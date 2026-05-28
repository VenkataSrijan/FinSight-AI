from enum import StrEnum


class AccountType(StrEnum):
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    CASH = "cash"
    INVESTMENT = "investment"
    CRYPTO = "crypto"


class CategoryType(StrEnum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class TransactionType(StrEnum):
    DEBIT = "debit"
    CREDIT = "credit"


class TransactionStatus(StrEnum):
    PENDING = "pending"
    POSTED = "posted"
    FAILED = "failed"


class TransactionSource(StrEnum):
    MANUAL = "manual"
    CSV_IMPORT = "csv_import"
    PLAID = "plaid"
    YODLEE = "yodlee"
    AI_EXTRACTED = "ai_extracted"