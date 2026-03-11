# Load package
library(rpart)

# Load dataset
data <- read.csv("pokemon.csv")

# Data cleanup
data <- na.omit(data)
data <- unique(data)

# Convert target column to factor
data$Legendary <- as.factor(data$Legendary)

# Build decision tree model
model <- rpart(Legendary ~ HP + Attack + Defense + Speed,
               data = data,
               method = "class")

# User input
hp <- as.numeric(readline("Enter HP: "))
attack <- as.numeric(readline("Enter Attack: "))
defense <- as.numeric(readline("Enter Defense: "))
speed <- as.numeric(readline("Enter Speed: "))

input <- data.frame(
  HP = hp,
  Attack = attack,
  Defense = defense,
  Speed = speed
)

# Prediction
result <- predict(model, newdata = input, type = "class")

print(result)
