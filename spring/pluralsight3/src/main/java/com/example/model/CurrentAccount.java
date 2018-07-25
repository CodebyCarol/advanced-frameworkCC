package com.example.model;

import com.example.application.Account;
import com.example.application.Card;

public class CurrentAccount implements Account {

    private Card creditCard;

    @Override
    public String createAccount() {
        return "CurrentAccount has been created";
    }


    public void setCreditCard(Card creditCard) {
        this.creditCard = creditCard;
    }
    @Override
    public String cardDetails() {
        return this.creditCard.cardDetails();
    }

}
