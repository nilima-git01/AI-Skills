package com.salesforce.tests;

import com.salesforce.pages.LoginPage;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import java.time.Duration;

public class InvalidLoginTest {

    private WebDriver driver;
    private LoginPage loginPage;

    @BeforeMethod
    public void setUp() throws Exception {
        try {
            ChromeOptions options = new ChromeOptions();
            options.addArguments("--remote-allow-origins=*");
            driver = new ChromeDriver(options);
            driver.manage().window().maximize();
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
            driver.get("https://login.salesforce.com/?locale=in");
            loginPage = new LoginPage(driver);
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }

    @Test
    public void testInvalidLogin() throws Exception {
        try {
            loginPage.doLogin("invaliduser@example.com", "InvalidPass123!", false);
            String actualErrorMsg = loginPage.getErrorMessage();
            Assert.assertTrue(actualErrorMsg.contains("check your username and password"), "Error message mismatch");
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }

    @AfterMethod
    public void tearDown() throws Exception {
        try {
            if (driver != null) {
                driver.quit();
            }
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }
}
