package com.example.model;

import com.example.application.Account;

public class SavingAccount implements Account {

    @Override
    public String createAccount(){
        return "Saving account created successfully.";
    }
}
