package database

import (
	"context"
	"fmt"
	"log"

"student-management-system/internal/config"

	"github.com/jackc/pgx/v5/pgxpool"
)

var DB *pgxpool.Pool

func Connect(cfg *config.Config) {
	dsn := fmt.Sprintf(
		"postgres://%s:%s@%s:%s/%s",
		cfg.DBUser,
		cfg.DBPassword,
		cfg.DBHost,
		cfg.DBPort,
		cfg.DBName,
	)

	pool, err := pgxpool.New(context.Background(), dsn)
	if err != nil {
		log.Fatal("Database connection failed:", err)
	}

	if err = pool.Ping(context.Background()); err != nil {
		log.Fatal("Unable to ping database:", err)
	}

	DB = pool

	var dbName, schema string

err = DB.QueryRow(context.Background(),
	"SELECT current_database(), current_schema()",
).Scan(&dbName, &schema)

if err != nil {
	log.Fatal(err)
}

log.Println("Database:", dbName)
log.Println("Schema:", schema)

	log.Println("✅ Connected to PostgreSQL")
}