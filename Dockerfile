# Stage 1: Build
FROM maven:3.9-eclipse-temurin-17 AS builder

WORKDIR /build

# Copy the pom.xml file first to cache the dependencies
COPY app/pom.xml .
RUN mvn dependency:go-offline -q

COPY app/src ./src
RUN mvn clean package -DskipTests -q

FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=builder /build/target/app-1.0-SNAPSHOT.jar app.jar

COPY .env* ./

ENTRYPOINT ["java", "-jar", "app.jar"]
