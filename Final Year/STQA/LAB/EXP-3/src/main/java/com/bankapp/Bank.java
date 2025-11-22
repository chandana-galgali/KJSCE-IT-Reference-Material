package com.bankapp;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.UUID;

/**
 * Manages all bank accounts and provides a command-line interface
 * for users to interact with the banking system.
 */
public class Bank {
    // Using a Map to store accounts, with the account number as the key for fast lookups.
    private Map<String, Account> accounts = new HashMap<>();
    private Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Bank bank = new Bank();
        bank.run(); // Start the application
    }

    /**
     * The main application loop that displays the menu and handles user input.
     */
    public void run() {
        System.out.println("Welcome to the Simple Banking App!");
        while (true) {
            printMenu();
            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    createAccount();
                    break;
                case "2":
                    depositToAccount();
                    break;
                case "3":
                    withdrawFromAccount();
                    break;
                case "4":
                    checkBalance();
                    break;
                case "5":
                    System.out.println("Thank you for using the Simple Banking App. Goodbye!");
                    return; // Exit the loop and the program
                default:
                    System.err.println("Invalid choice. Please enter a number between 1 and 5.");
            }
            System.out.println(); // Add a blank line for readability
        }
    }

    private void printMenu() {
        System.out.println("--------------------");
        System.out.println("1. Create New Account");
        System.out.println("2. Deposit Funds");
        System.out.println("3. Withdraw Funds");
        System.out.println("4. Check Balance");
        System.out.println("5. Exit");
        System.out.println("--------------------");
    }

    private void createAccount() {
        System.out.print("Enter account holder's name: ");
        String name = scanner.nextLine();

        // Generate a simple unique account number
        String accountNumber = "ACC-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

        Account newAccount = new Account(accountNumber, name, 0.0);
        accounts.put(accountNumber, newAccount);

        System.out.println("✅ Account created successfully!");
        System.out.println("Your new account number is: " + accountNumber);
    }

    private Account findAccount() {
        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();
        Account account = accounts.get(accountNumber);
        if (account == null) {
            System.err.println("❌ Account not found.");
        }
        return account;
    }

    private void depositToAccount() {
        Account account = findAccount();
        if (account != null) {
            try {
                System.out.print("Enter amount to deposit: ");
                double amount = Double.parseDouble(scanner.nextLine());
                if (account.deposit(amount)) {
                    System.out.printf("✅ Deposit successful. New balance: $%.2f%n", account.getBalance());
                }
            } catch (NumberFormatException e) {
                System.err.println("❌ Invalid amount. Please enter a number.");
            }
        }
    }

    private void withdrawFromAccount() {
        Account account = findAccount();
        if (account != null) {
            try {
                System.out.print("Enter amount to withdraw: ");
                double amount = Double.parseDouble(scanner.nextLine());
                if (account.withdraw(amount)) {
                    System.out.printf("✅ Withdrawal successful. New balance: $%.2f%n", account.getBalance());
                }
            } catch (NumberFormatException e) {
                System.err.println("❌ Invalid amount. Please enter a number.");
            }
        }
    }

    private void checkBalance() {
        Account account = findAccount();
        if (account != null) {
            System.out.println("Account Details:");
            System.out.println(account); // Uses the overridden toString() method in Account
        }
    }
}