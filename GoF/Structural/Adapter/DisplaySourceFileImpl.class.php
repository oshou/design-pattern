<?php

require_once 'DisplaySourceFile.class.php';
require_once 'ShowFile.class.php';

/**
 * DisplaySourceFileを実装したクラス
 */
class DisplaySourceFileImpl extends showFile implements DisplaySourceFile
{
    /**
     * コンストラクタ
     */
    public function __contruct($filename)
    {
        parent::__construct($filename);
    }

    /**
     * 指定されたソースファイルをハイライト表示する
     */
    public function display()
    {
        parent::showHighlight();
    }
}
