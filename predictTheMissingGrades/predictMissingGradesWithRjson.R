train <- readLines("training.json", n=-1)
train <- train[c(2 : length(train))]
train <- sprintf("[%s]",paste(train,collapse = ','))
library(rjson)
train <- rjson::fromJSON(train)

listtoDF <- function(xmas, columns, colclass){
  comby <- data.frame(matrix(NA, nrow = length(xmas), ncol = length(columns)))
  #comby <- read.table(text = '', colClasses = colclass, col.names = columns)
  names(comby) <- columns
  for(i in 1:length(xmas)){
    comby[i,names(xmas[[i]])] <- xmas[[i]]
  }
  return(comby)
}
columns <- c("Physics", "Chemistry", "PhysicalEducation", "English", 
             "Mathematics", "serial", "ComputerScience", "Hindi", "Biology", 
             "Economics", "Accountancy", "BusinessStudies")
colclass <- rep("numeric",12)

train <- listtoDF(train, columns, colclass)
train <- train[-6]
train[is.na(train)] <- 0
train[] <- lapply(train, factor)

test <- readLines("sample-test.in.json", n=-1)
test <- test[c(2 : length(test))]
test <- sprintf("[%s]",paste(test,collapse = ','))
test <- rjson::fromJSON(test)
test <- listtoDF(test,columns, colclass)
test <- test[-6]
test[is.na(test)] <- 0
test[] <- lapply(test, factor)


library(rpart)
model <- rpart(Mathematics ~ ., data = train, method = 'class')
out <- predict(model, test, type = 'class')

out <- as.numeric(out)
for(i in 1:floor(length(out)/1000)){
  write(out[i], stdout())
}
