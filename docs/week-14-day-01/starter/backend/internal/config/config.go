package config

import (
	"log/slog"
	"os"

	"github.com/joho/godotenv"
)

// Config holds process settings from the environment.
type Config struct {
	Port       string
	JWTSecret  string
	DBHost     string
	DBPort     string
	DBUser     string
	DBPassword string
	DBName     string
}

// Load reads optional .env then environment variables.
func Load() *Config {
	if err := godotenv.Load(); err != nil {
		slog.Info("no .env file; using process environment")
	}

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	dbPort := os.Getenv("DB_PORT")
	if dbPort == "" {
		dbPort = "5432"
	}
	dbHost := os.Getenv("DB_HOST")
	if dbHost == "" {
		dbHost = "localhost"
	}
	dbUser := os.Getenv("DB_USER")
	if dbUser == "" {
		dbUser = "postgres"
	}
	dbName := os.Getenv("DB_NAME")
	if dbName == "" {
		dbName = "sms"
	}

	return &Config{
		Port:       port,
		JWTSecret:  os.Getenv("JWT_SECRET"),
		DBHost:     dbHost,
		DBPort:     dbPort,
		DBUser:     dbUser,
		DBPassword: os.Getenv("DB_PASSWORD"),
		DBName:     dbName,
	}
}
