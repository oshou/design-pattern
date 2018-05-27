<?php

require_once 'DisplaySourceFileImpl.class.php';

/**
 * DisplaySourceFileImplクラスをインスタンス化する
 * 内容お表示するクラスはShowFile.class.php
 */
$show_file = new DisplaySourceFileImpl('./ShowFile.class.php');

/**
 * プレーンテキストとハイライトしたファイル内容をそれぞれ表示する
 */
$show_file->display();
