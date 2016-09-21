library(XML)

home_df <- data.frame(Name = character(), Gender = character(),
                      Friends = character(), Work = character(), 
                      Education = character(), Lives_in = character(), Hometown = character(),
                      stringsAsFactors=FALSE)

#link <- "/Users/apple/Dropbox/urap_programming/FB_fake_like/suyang/URAP_fa16/out/abbey.breshears_home.html"

setwd("/Users/apple/Dropbox/urap_programming/FB_fake_like/suyang/URAP_fa16/out")
list <- list.files(pattern="_home.html")

for (i in list){
  link <- paste("/Users/apple/Dropbox/urap_programming/FB_fake_like/suyang/URAP_fa16/out/",i,sep="")
  #link <- "/Users/apple/Dropbox/urap_programming/FB_fake_like/suyang/URAP_fa16/out/abbey.breshears_home.html"
  
  doc <- htmlParse(link)
  root <- xmlRoot(doc)
  
  user <- root %>% xpathSApply("/html/body//div[@title='Facebook']", xmlValue)
  user <- sub("(.*)/(.*)","\\2",user)

  name <- root %>% xpathSApply("/html/head/title", xmlValue) 

  gender <- root %>% xpathSApply("/html/body//div[@title='Gender']", xmlValue)
  if(is.null(gender) | length(gender)== 0){
    gender <- NA
  }else{
    gender <- substr(gender, 7, nchar(gender))
  }

  friends <- root %>% xpathSApply(paste("/html/body//a[@href='/",user,"/friends']",sep=""), xmlValue)
  if(is.null(friends) | length(friends)== 0){
    num_friends <- NA
  }else{
    num_friends <- gsub("[A-Za-z \\(\\)]","",friends)[2]
  }

  work <- root %>% xpathSApply("/html/body//div[@id='work']//div[@class='cx cy']", xmlValue)
  work <- gsub("([A-Za-z0-9])([A-Z][a-z])","\\1; \\2", work[work != ""])
  work <- gsub("([A-Za-z])([0-9])","\\1; \\2", work)
  work <- paste(work, collapse = ". ")

  education <- root %>% xpathSApply("/html/body//div[@id='education']//div[@class='cx cy']", xmlValue)
  education <- gsub("([A-Za-z0-9])([A-Z][a-z])","\\1; \\2", education[education != ""])
  education <- gsub("([A-Za-z])([0-9])","\\1; \\2", education)
  education <- paste(education, collapse = ". ")

  current_city <- root %>% xpathSApply("/html/body//div[@title='Current City']//a", xmlValue)
  if(is.null(current_city)) current_city <- NA

  hometown <- root %>% xpathSApply("/html/body//div[@title='Hometown']//a", xmlValue)
  if(is.null(hometown)) hometown <- NA

  entries <- c(name,
               gender,
               num_friends,
               work,
               education,
               current_city,
               hometown)

  home_df[nrow(home_df)+1, ] <- entries
}

