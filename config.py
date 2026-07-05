# config.py
# ============================================================
# KRISHNA KILLING SPREE — CONFIGURACIÓN GLOBAL
# ============================================================

# ---- ACTIVOS ----
SYMBOLS = [
    "BTC-USDT-SWAP",
    "ETH-USDT-SWAP",
    "SOL-USDT-SWAP",
    "ADA-USDT-SWAP",
    "XRP-USDT-SWAP",
    "AVAX-USDT-SWAP",
]

# ---- APALANCAMIENTO ----
BASE_LEVERAGE = 7
CAPITAL_INICIAL = 100.0

# ---- ESTRATEGIA ----
MIN_SCORE = 0.45
TP_MULT = 1.2
SL_MULT = 1.0
EMA_FAST = 20
EMA_SLOW = 50
ATR_PERIOD = 14
ADX_PERIOD = 14
MOMENTUM_PERIOD = 5
COOLDOWN_SECONDS = 15 * 60

# ---- CONTROL DE DRAWDOWN ----
DD_NORMAL_LIMIT = 8.0
DD_REDUCED_LIMIT = 12.0
DD_KILL_LIMIT = 15.0

LEVERAGE_NORMAL = 7
LEVERAGE_REDUCED = 3
LEVERAGE_PROTECTION = 1

SIZE_FACTOR_NORMAL = 1.0
SIZE_FACTOR_REDUCED = 0.6
SIZE_FACTOR_PROTECTION = 0.2

KILL_THRESHOLD = 15.0
KILL_SWITCH_ENABLED = True

# ---- DIRECTORIOS ----
METRICS_DIR = "metrics"
LOGS_DIR = "logs"
SNAPSHOTS_DIR = "snapshots"

# ============================================================
# 🆕 GESTIÓN TEMPORAL DE POSICIONES
# ============================================================

# Tiempo mínimo antes de evaluar break-even (minutos)
BREAK_EVEN_MINUTES = 10

# Tiempo máximo de permanencia (minutos)
MAX_HOLD_MINUTES = 60

# Buffer de seguridad para break-even (% sobre capital)
# Se suma a comisiones+slippage para asegurar PnL positivo
BREAK_EVEN_BUFFER = 0.05  # 0.05%

# Frecuencia de evaluación (segundos)
EVALUATION_INTERVAL = 30
