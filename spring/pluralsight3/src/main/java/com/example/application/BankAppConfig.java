package com.example.application;

import com.example.model.CreditCard;
import com.example.model.CurrentAccount;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Scope;

public class BankAppConfig {

    @Bean
    public CreditCard creditCard(){
        return new CreditCard();
    }

    @Bean(initMethod ="onInit", destroyMethod ="onDestroy")
    @Scope("prototype")
    public CurrentAccount currentAccount(){
        return new CurrentAccount();
    }


}
