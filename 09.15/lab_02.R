#문제1

m1 <- matrix(seq(10,38,2),nrow = 3,ncol = 5,byrow = T)
m2 <- m1 + 100
m_max_v <- max(m1)
m_min_v <- min(m1)
row_max <- apply(m1,1,max)
col_max <- apply(m1,2,max)
m1;m2;m_max_v;m_min_v;row_max;col_max

#문제2
n1 <- c(1,2,3)
n2 <- c(4,5,6)
n3 <- c(7,8,9)
m2 <- matrix(cbind(n1,n2,n3),nrow=3)
m2

#문제3
