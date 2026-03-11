# Load dataset
data <- read.csv("SalaryData.csv")

# Data cleanup
data <- na.omit(data)
data <- unique(data)

# Train-test split
set.seed(123)
index <- sample(1:nrow(data), 0.8 * nrow(data))
train <- data[index, ]
test <- data[-index, ]

# Linear regression model
model <- lm(Salary ~ YearsExperience, data = train)

# Model accuracy
summary_model <- summary(model)
cat("Adjusted R-squared:", round(summary_model$adj.r.squared, 3), "\n")

# Prediction on test data
pred <- predict(model, newdata = test)

mae <- mean(abs(test$Salary - pred))
rmse <- sqrt(mean((test$Salary - pred)^2))

cat("MAE:", round(mae,2), "\n")
cat("RMSE:", round(rmse,2), "\n")

# User input prediction
yoe <- as.numeric(readline("Enter Years of Experience: "))
result <- predict(model, data.frame(YearsExperience = yoe))

cat("Predicted Salary:", round(result,2), "\n")
