x_input<-readline("enter nos separated by spaces:")
y_input<-readline("enter nos separated by spaces:")
x<-as.integer(strsplit(x_input," ")[[1]])
y<-as.integer(strsplit(y_input," ")[[1]])
n<-length(x)
mx<-sum(x)/n
my<-sum(y)/n

var_x<-sum((x-mx)^2)/(n-1)
var_y<-sum((y-my)^2)/(n-1)
cov<-sum((x-mx)*(y-my))/(n-1)
cor<-cov/(sqrt(var_x)*sqrt(var_y))
print(cov)
print(cor)
