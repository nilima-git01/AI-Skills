package com.salesforce.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class LoginPage {
    private WebDriver driver;
    private WebDriverWait wait;

    @FindBy(xpath = "//input[@id='username']")
    WebElement username;

    @FindBy(xpath = "//input[@id='password']")
    WebElement password;
    
    @FindBy(xpath = "//input[@id='rememberUn']")
    WebElement rememberMeCheckbox;

    @FindBy(xpath = "//input[@id='Login']")
    WebElement loginButton;

    @FindBy(xpath = "//div[@id='error']")
    WebElement errorMessage;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(15));
        PageFactory.initElements(driver, this);
    }

    public void doLogin(String user, String pass, boolean rememberMe) throws Exception {
        try {
            wait.until(ExpectedConditions.visibilityOf(username)).sendKeys(user);
            wait.until(ExpectedConditions.visibilityOf(password)).sendKeys(pass);
            if (rememberMe) {
                if (!rememberMeCheckbox.isSelected()) {
                    wait.until(ExpectedConditions.elementToBeClickable(rememberMeCheckbox)).click();
                }
            } else {
                if (rememberMeCheckbox.isSelected()) {
                    wait.until(ExpectedConditions.elementToBeClickable(rememberMeCheckbox)).click();
                }
            }
            wait.until(ExpectedConditions.elementToBeClickable(loginButton)).click();
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }

    public String getErrorMessage() throws Exception {
        try {
            return wait.until(ExpectedConditions.visibilityOf(errorMessage)).getText();
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }
}
