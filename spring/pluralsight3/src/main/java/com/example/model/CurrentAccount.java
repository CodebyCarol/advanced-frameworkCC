package com.example.model;

import com.example.application.Account;
import com.example.application.Card;
import org.springframework.beans.factory.annotation.Autowired;

public class CurrentAccount implements Account {

    @Autowired
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

    public void onInit(){
        System.out.println("onInit method on CurrentAccount has been invoked");
    }

    public void onDestroy(){
        System.out.println("onDestroy method on CurrentAcount has been invoked");
    }
}
