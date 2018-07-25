package com.example.model;

import com.example.application.Card;

public class CreditCard implements Card {

    @Override
    public String cardDetails() {
        return "Credit Card has been issued";
    }
}
