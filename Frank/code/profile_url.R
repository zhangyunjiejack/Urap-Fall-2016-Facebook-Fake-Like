profile <- read.csv("/Users/apple/Dropbox/urap_programming/FB_fake_like/Frank/input/profile_url.csv")

id <- gsub("(.*com)(.*?)\\?ref.*","\\2",profile$url)
home <- gsub("(^.*?)\\?ref.*","\\1",profile$url)
friends <- paste("http://www.facebook.com",id,"/friends", sep="")
likes <- paste("http://www.facebook.com",id,"/likes", sep="")
about <- paste("http://www.facebook.com",id,"/about", sep="")

df <- data.frame(id=id, home=home, friends=friends, likes=likes, about=about)

write.csv(df, "/Users/apple/Dropbox/urap_programming/FB_fake_like/Frank/output/profile_url_basic.csv", row.names = FALSE)
