# Gherkin.feature
Feature: 百度

  Scenario: 场景1-搜索关键字

    Given 关键字:behave自动化测试
    When 打开百度页面:https://www.baidu.com
    And 输入关键字
    And 点击百度一下按钮
    Then 页面中应包含关键字:behave

    Scenario: 多浏览器操作
      When 浏览器1 打开百度页面:https://www.baidu.com
      And 浏览器2 打开百度页面:https://www.baidu.com
      And 浏览器1 输入关键字 behave自动化测试
      And 浏览器2 输入关键字 httprunner接口测试
      And 浏览器1 点击百度一下按钮
      And 浏览器2 点击百度一下按钮
      Then 浏览器1 页面中应包含关键字:behave
      And 浏览器2 页面中应包含关键字:httprunner