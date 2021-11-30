require(graphics)

CAMEROONSPLINE <- read_excel("Downloads/CAMEROONSPLINE.xlsx")
op <- par(mfrow = c(2,1), mgp = c(2,.8,0), mar = 0.1+c(3,3,3,1))
require(splines)
Week <- CAMEROONSPLINE$Weeks
Cases <- CAMEROONSPLINE$NewCases
plot(Week, Cases, main = paste("spline for Cameroon COVID-19 daily new cases"))
lines(spline(Week, Cases))
lines(spline(Week, Cases, n = 201), col = 2)
fit<-lm(Cases ~ bs(Week,knots = c(25,40,60)),data = CAMEROONSPLINE )
fit1<-smooth.spline(Week,Cases,df=10) 
#Plotting both cubic and Smoothing Splines 
plot(Week,Cases,col="grey",xlab="Week",ylab="Cases")
points(Week,predict(fit,newdata = list(Week=Week)),col="darkgreen",lwd=2,type="l")
#adding cutpoints
abline(v=c(25,40,60),lty=2,col="darkgreen")
lines(fit1,col="red",lwd=2)
legend("topleft",c("Smoothing Spline with 16 df","Cubic Spline"),col=c("red","darkgreen"),lwd=2)
fit2<-smooth.spline(Week,Cases,cv = TRUE)
fit2

plot(Week,Cases,col="grey")
#Plotting Regression Line
lines(fit2,lwd=2,col="purple")
legend("topright",("Smoothing Splines selected by CV"),col="purple",lwd=2)
library(npreg)
mod.ss <- ss(Week,Cases, nknots = 10)
mod.ss
mod.smsp <- smooth.spline(Week,Cases, nknots = 10)
mod.smsp
# rmse between solutions
sqrt(mean(( mod.ss$y - mod.smsp$y )^2))


plot(Week,Cases)
lines(Week, mod.ss$y, lty = 2, col = 2, lwd = 2)
lines(Week, mod.smsp$y, lty = 3, col = 3, lwd = 2)
legend("topright", 
       legend = c( "ss", "smooth.spline"), 
       lty = 2:3, col = 2:3, lwd = 2, bty = "n")

plot(mod.ss, xlab = "Week", ylab = "Cases")
# summary method
mod.sum <- summary(mod.ss)
mod.sum

# subplots (1 x 3)
par(mfrow = c(1,2))


# GCV selection
mod.ss <- ss(Week,Cases, all.knots = TRUE)
plot(mod.ss, ylim = c(0, 130))
points(Week,Cases)

# lambda = 100 (df = m)
mod.ss10 <- ss(Week,Cases, all.knots = TRUE, lambda = 100)
plot(mod.ss10, ylim = c(0, 130))
points(Week,Cases)

mod.lin <- ss(Week,Cases, nknots = 10, m = 1)
mod.cub <- ss(Week,Cases, nknots = 10)
mod.qui <- ss(Week,Cases, nknots = 10, m = 3)
par(mfrow = c(1,3))
plot(mod.lin, ylim = c(0, 130))
points(Week,Cases)
plot(mod.cub, ylim = c(0, 130))
points(Week,Cases)
plot(mod.qui, ylim = c(0, 130))
points(Week,Cases)

# plot ss fit
plot(mod.ss, xlab = "Week", ylab = "Cases")

# add lm fit
abline(coef(lm(Cases ~ Week, data = CAMEROONSPLINE)), lty = 2)

# add data and legend
with(CAMEROONSPLINE, points(Week,Cases))
legend("bottomright", legend = c("ss", "lm"), lty = 1:2, bty = "n")
# fit model
mod.ss <- with(CAMEROONSPLINE, ss(Week,Cases))
mod.ss
# summarize fit
summary(mod.ss)

