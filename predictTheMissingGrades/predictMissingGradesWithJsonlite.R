train <- readLines("training.json", n=-1)
train <- train[c(2 : length(train))]
train <- sprintf("[%s]",paste(train,collapse = ','))
library(jsonlite)
train <- jsonlite::fromJSON(train)
train <- train[-6]
train[is.na(train)] <- 0
train[] <- lapply(train, factor)

test <- readLines("sample-test.in.json", n=-1)
number <- as.numeric(test[1])
test <- test[c(2 : length(test))]
test <- sprintf("[%s]",paste(test,collapse = ','))
test <- jsonlite::fromJSON(test)
test <- test[-5]
test[is.na(test)] <- 0
test[] <- lapply(test, factor)
test$Mathematics <- NA

columns <- colnames(train)
test <- test[columns]

library(rpart)
model <- rpart(Mathematics ~ ., data = train, method = 'class')
out <- predict(model, test, type = 'class')

out <- as.numeric(out)
for(i in 1:length(out)){
  write(out[i], stdout())
}
