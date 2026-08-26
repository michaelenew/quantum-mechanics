
#include <stdint.h>
#include <math.h>
#define PI 3.14159265358979323846

static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t xnext(uint64_t* s){
    uint64_t r = rotl(s[1]*5ULL,7)*9ULL;
    uint64_t t = s[1]<<17;
    s[2]^=s[0]; s[3]^=s[1]; s[1]^=s[2]; s[0]^=s[3];
    s[2]^=t; s[3]=rotl(s[3],45);
    return r;
}
static double u01(uint64_t* s){
    return (double)(xnext(s)>>11)*(1.0/9007199254740992.0);
}
static double gauss(uint64_t* s){
    double u = 1.0-u01(s), v = u01(s);
    return sqrt(-2.0*log(u))*cos(2.0*PI*v);
}
static inline void qmul(const double* a,const double* b,double* o){
    o[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3];
    o[1]=a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2];
    o[2]=a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1];
    o[3]=a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0];
}
static inline void qcj(const double* a,double* o){
    o[0]=a[0]; o[1]=-a[1]; o[2]=-a[2]; o[3]=-a[3];
}
/* bilinear lookup on the 2-D log-weight table, indexed by the two
   class angles */
static inline double lnw2(const double* T,int n,double wp,double wm){
    if(wp>1.0)wp=1.0; if(wp<-1.0)wp=-1.0;
    if(wm>1.0)wm=1.0; if(wm<-1.0)wm=-1.0;
    double xp=acos(wp)*(n-1)/PI, xm=acos(wm)*(n-1)/PI;
    int i=(int)xp, j=(int)xm;
    if(i>n-2)i=n-2; if(i<0)i=0;
    if(j>n-2)j=n-2; if(j<0)j=0;
    double fi=xp-i, fj=xm-j;
    const double* r0=T+(long)i*n; const double* r1=T+(long)(i+1)*n;
    return (1-fi)*((1-fj)*r0[j]+fj*r0[j+1])
         +    fi *((1-fj)*r1[j]+fj*r1[j+1]);
}
static inline void rnd_rot(uint64_t* rs,double sig,double* rot){
    double ang = sig*gauss(rs);
    double a0=gauss(rs),a1=gauss(rs),a2=gauss(rs);
    double n=sqrt(a0*a0+a1*a1+a2*a2);
    if(n<1e-12){a0=1;a1=0;a2=0;n=1;}
    double c=cos(0.5*ang), sn=sin(0.5*ang)/n;
    rot[0]=c; rot[1]=sn*a0; rot[2]=sn*a1; rot[3]=sn*a2;
}

/* lp, lm: [((mu*V)+s)*4 + c].  up/dn: [mu*V + s]. */
void sweeps4f(const unsigned char* frz,double* lp,double* lm,const int32_t* up,const int32_t* dn,
             int V,int nsweeps,double sig,const double* T,int ntab,
             uint64_t* rs,long* acc_out,long* tot_out)
{
    long acc=0, tot=0;
    for(int sw=0; sw<nsweeps; sw++){
      for(int mu=0; mu<4; mu++){
        for(int s=0; s<V; s++){
          if(frz[(long)(mu*V)+s]) continue;
          double* Up = lp + ((long)(mu*V)+s)*4;
          double* Um = lm + ((long)(mu*V)+s)*4;
          double rp[4], rm[4], Pp[4], Pm[4];
          rnd_rot(rs,sig,rp); rnd_rot(rs,sig,rm);
          qmul(rp,Up,Pp); qmul(rm,Um,Pm);
          double dln=0.0, t1[4],t2[4],SP[4],SM[4],qp[4],qm[4];
          for(int nu=0; nu<4; nu++){
            if(nu==mu) continue;
            int smu = up[mu*V+s], snu = up[nu*V+s];
            /* forward: S = U_nu(s+mu) U_mu(s+nu)^+ U_nu(s)^+ */
            qcj(lp+((long)(mu*V)+snu)*4,t1);
            qmul(lp+((long)(nu*V)+smu)*4,t1,t2);
            qcj(lp+((long)(nu*V)+s)*4,t1); qmul(t2,t1,SP);
            qcj(lm+((long)(mu*V)+snu)*4,t1);
            qmul(lm+((long)(nu*V)+smu)*4,t1,t2);
            qcj(lm+((long)(nu*V)+s)*4,t1); qmul(t2,t1,SM);
            qmul(Up,SP,qp); qmul(Um,SM,qm);
            double lo = lnw2(T,ntab,qp[0],qm[0]);
            qmul(Pp,SP,qp); qmul(Pm,SM,qm);
            dln += lnw2(T,ntab,qp[0],qm[0]) - lo;
            /* backward, base b = s-nu:
               S = U_nu(b+mu)^+ U_mu(b)^+ U_nu(b) */
            int b = dn[nu*V+s], bmu = up[mu*V+b];
            qcj(lp+((long)(nu*V)+bmu)*4,t1);
            qcj(lp+((long)(mu*V)+b)*4,t2);
            qmul(t1,t2,SP);
            qmul(SP,lp+((long)(nu*V)+b)*4,t1);
            SP[0]=t1[0];SP[1]=t1[1];SP[2]=t1[2];SP[3]=t1[3];
            qcj(lm+((long)(nu*V)+bmu)*4,t1);
            qcj(lm+((long)(mu*V)+b)*4,t2);
            qmul(t1,t2,SM);
            qmul(SM,lm+((long)(nu*V)+b)*4,t1);
            SM[0]=t1[0];SM[1]=t1[1];SM[2]=t1[2];SM[3]=t1[3];
            qmul(Up,SP,qp); qmul(Um,SM,qm);
            lo = lnw2(T,ntab,qp[0],qm[0]);
            qmul(Pp,SP,qp); qmul(Pm,SM,qm);
            dln += lnw2(T,ntab,qp[0],qm[0]) - lo;
          }
          tot++;
          if(log(u01(rs)+1e-300) < dln){
            for(int c=0;c<4;c++){ Up[c]=Pp[c]; Um[c]=Pm[c]; }
            acc++;
          }
        }
      }
    }
    *acc_out += acc; *tot_out += tot;
}
