package com.bankapp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AccountTest {

    private Account account;

    @BeforeEach
    void setUp() {
        // Create a fresh account with a starting balance for each test
        account = new Account("ACC-123", "John Doe", 500.00);
    }

    // --- Original "Happy Path" Tests ---
    @Test
    void testSuccessfulDeposit() {
        assertTrue(account.deposit(100.00));
        assertEquals(600.00, account.getBalance());
    }

    @Test
    void testSuccessfulWithdrawal() {
        assertTrue(account.withdraw(200.00));
        assertEquals(300.00, account.getBalance());
    }

    // --- ADDITIONAL TESTS TO KILL ALL MUTANTS ---

    @Test
    void testDepositWithNegativeAmount() {
        assertFalse(account.deposit(-50.00));
        assertEquals(500.00, account.getBalance());
    }
    
    @Test
    void testDepositZeroAmount() {
        assertFalse(account.deposit(0));
        assertEquals(500.00, account.getBalance());
    }

    @Test
    void testWithdrawWithNegativeAmount() {
        assertFalse(account.withdraw(-50.00));
        assertEquals(500.00, account.getBalance());
    }
    
    @Test
    void testWithdrawInsufficientFunds() {
        assertFalse(account.withdraw(1000.00));
        assertEquals(500.00, account.getBalance());
    }

    @Test
    void testWithdrawExactBalance() {
        assertTrue(account.withdraw(500.00));
        assertEquals(0.00, account.getBalance());
    }

    @Test
    void testWithdrawZeroAmount() {
        assertFalse(account.withdraw(0));
        assertEquals(500.00, account.getBalance());
    }
}