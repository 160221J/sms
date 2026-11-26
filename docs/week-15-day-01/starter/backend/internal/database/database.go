package database

import (
	"context"
	"fmt"
	"log/slog"
	"time"

	"student-management-system/internal/config"

	"github.com/jackc/pgx/v5/pgxpool"
)

// Connect opens a pgx pool and pings Postgres (week 14).
func Connect(ctx context.Context, cfg *config.Config) (*pgxpool.Pool, error) {
	dsn := fmt.Sprintf(
		"postgres://%s:%s@%s:%s/%s?sslmode=disable",
		cfg.DBUser,
		cfg.DBPassword,
		cfg.DBHost,
		cfg.DBPort,
		cfg.DBName,
	)

	poolCfg, err := pgxpool.ParseConfig(dsn)
	if err != nil {
		return nil, fmt.Errorf("parse dsn: %w", err)
	}
	poolCfg.MaxConns = 10
	poolCfg.MinConns = 1
	poolCfg.MaxConnLifetime = time.Hour

	pool, err := pgxpool.NewWithConfig(ctx, poolCfg)
	if err != nil {
		return nil, fmt.Errorf("connect: %w", err)
	}
	if err := pool.Ping(ctx); err != nil {
		pool.Close()
		return nil, fmt.Errorf("ping: %w", err)
	}

	var dbName, schema string
	if err := pool.QueryRow(ctx, "SELECT current_database(), current_schema()").Scan(&dbName, &schema); err != nil {
		pool.Close()
		return nil, err
	}
	slog.Info("connected to postgresql", "database", dbName, "schema", schema)
	return pool, nil
}
