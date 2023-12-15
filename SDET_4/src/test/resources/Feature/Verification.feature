Feature: Image Verification

  Scenario: Verify Image in IFRAME
    Given I launch the URL "http://webdriveruniversity.com/index.html"
    When I click on the IFRAME link
    Then a new tab should open and switch to that tab
    And I verify that the image is present
    And I click on the right arrow button to change the image

