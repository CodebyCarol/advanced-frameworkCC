package com.example.model;

import com.example.application.Account;
import com.example.application.Card;

public class SavingAccount implements Account {

    private Card atmCard;

    public SavingAccount(Card card) {
        atmCard = card;
    }

    @Override
    public String createAccount(){
        return "Saving account created successfully.";
    }

    @Override
    public String cardDetails() {
        return atmCard.cardDetails();
    }
}
