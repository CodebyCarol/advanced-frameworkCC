package com.example.model;

import com.example.application.Account;

public class CurrentAccount implements Account {

    @Override
    public String createAccount() {
        return "CurrentAccount has been created";
    }
}
