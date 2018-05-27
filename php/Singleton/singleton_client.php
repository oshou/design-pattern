<?php

require_once 'SingletonSample.class.php';

/**
 * インスタンスを2つ取得する
 */
$instance1 = SingletonSample::getInstance();
sleep(1);
$instance2 = SingletonSample::getInstance();

echo '<hr>';

/**
 * 2つのインスタンスIDが同一か確認する
 */
echo 'instance1-ID: '.$instance1->getID()."<br>";
echo 'instance2-ID: '.$instance2->getID()."<br>";
echo 'instance1->getID() === $instance2->getID(): '.($instance1->getID() === $instance2->getID() ? 'true' : 'false')."<br>";

/**
 * 2つのインスタンスが同一か確認する
 */
echo 'instance1 === instance2: '.($instance1 === $instance2 ? 'true' : 'false').PHP_EOL;
echo '<hr>';

/**
 * 複製出来ない事を確認する
 */
$instance1_clone = clone $instance1;
