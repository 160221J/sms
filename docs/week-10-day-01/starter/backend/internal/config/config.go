package config

import (
	"log/slog"
	"os"

	"github.com/joho/godotenv"
)

// Config holds process settings from the environment.
type Config struct {
	Port      string
	JWTSecret string
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

	return &Config{
		Port:      port,
		JWTSecret: os.Getenv("JWT_SECRET"),
	}
}
