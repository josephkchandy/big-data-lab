# Load dataset
data <- read.csv("car_data.csv")

# Data cleanup
data <- na.omit(data)
data <- unique(data)

# Convert gender to factor
data$Gender <- as.factor(data$Gender)

# Build logistic regression model
model <- glm(Purchased ~ Gender + Age + EstimatedSalary,
             data = data,
             family = binomial)

# User input
g <- readline("Enter Gender (Male/Female): ")
a <- as.numeric(readline("Enter Age: "))
s <- as.numeric(readline("Enter Salary: "))

input <- data.frame(
  Gender = factor(g, levels = levels(data$Gender)),
  Age = a,
  EstimatedSalary = s
)

# Prediction
prob <- predict(model, newdata = input, type = "response")

if(prob > 0.5){
  print("Customer will purchase")
} else {
  print("Customer will not purchase")
}
