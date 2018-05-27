<?php

/**
 * http://d.hatena.ne.jp/shimooka/20141212/1418363698
 */

abstract class AbstractDisplay
{
    /**
     * 表示するデータ
     */
    private $data;


    /**
     * コンストラクタ
     * @param mixed 表示するデータ
     */
    public function __construct($data)
    {
        if (!is_array($data)) {
            $data = array($data);
        }
        $this->data = $data;
    }


    /**
     * データ取得
     */
    public function getData()
    {
        return $this->data;
    }


    /**
     * Template Method
     */
    public function display()
    {
        $this->displayHeader();
        $this->displayBody();
        $this->displayFooter();
    }


    /**
     * ヘッダ表示用 抽象メソッド
     *
     * 実装はサブクラスで行う
     */
    abstract protected function displayHeader();


    /**
     * ボディ表示用 抽象メソッド
     *
     * 実装はサブクラスで行う
     */
    abstract protected function displayBody();


    /**
     * フッタ表示用 抽象メソッド
     *
     * 実装はサブクラスで行う
     */
    abstract protected function displayFooter();
}
