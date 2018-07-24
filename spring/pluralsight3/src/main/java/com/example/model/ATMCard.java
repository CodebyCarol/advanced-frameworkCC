package com.example.model;

import com.example.application.Card;

public class ATMCard implements Card {

    @Override
    public String cardDetails() {
        return "******************ATM Card has been issued";
    }
}
