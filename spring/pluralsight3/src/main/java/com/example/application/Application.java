package com.example.application;

import com.example.model.CurrentAccount;
import com.example.model.SavingAccount;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		// SavingAccount savingAccount = new SavingAccount();

		Account savingAccount = new SavingAccount();
		Account currentAccount = new CurrentAccount();

		System.out.println(savingAccount.createAccount());
		System.out.println(currentAccount.createAccount());
		// SpringApplication.run(Application.class, args);
	}
}
