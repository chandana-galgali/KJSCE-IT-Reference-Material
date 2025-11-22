package com.bankapp;

/**
 * Represents a single bank account.
 * This class handles the core data and logic for an account,
 * such as its number, owner, and balance.
 */
public class Account {
    // --- Attributes ---
    private String accountNumber;
    private String accountHolderName;
    private double balance;

    // --- Constructor ---
    public Account(String accountNumber, String accountHolderName, double initialDeposit) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = initialDeposit;
    }

    // --- Getters (to access private data safely) ---
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolderName() {
        return accountHolderName;
    }

    public double getBalance() {
        return balance;
    }

    // --- Core Functionality (Methods) ---

    /**
     * Adds funds to the account.
     * @param amount The amount to deposit. Must be positive.
     * @return true if the deposit was successful, false otherwise.
     */
    public boolean deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
            return true;
        } else {
            System.err.println("Deposit amount must be positive.");
            return false;
        }
    }

    /**
     * Withdraws funds from the account.
     * @param amount The amount to withdraw. Must be positive and not exceed the balance.
     * @return true if the withdrawal was successful, false otherwise.
     */
    public boolean withdraw(double amount) {
        if (amount <= 0) {
            System.err.println("Withdrawal amount must be positive.");
            return false;
        }
        if (amount > this.balance) {
            System.err.println("Insufficient funds. Current balance: " + this.balance);
            return false;
        }
        this.balance -= amount;
        return true;
    }

    @Override
    public String toString() {
        return String.format("Account [Number: %s, Holder: %s, Balance: $%.2f]",
                accountNumber, accountHolderName, balance);
    }
}