pal<-function(s){
    s==paste(rev(strsplit(s,"")[[1]]),collapse='')
}
word<-'madam'
cat(word,"is a palindrome",pal(word))
