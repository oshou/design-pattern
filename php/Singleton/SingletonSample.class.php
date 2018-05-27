<?php

/**
 * http://d.hatena.ne.jp/shimooka/20141212/1418363981
 *
 * @author test
 */
class SingletonSample
{
    private $id;

    /**
     * 唯一のインスタンスを保持
     */
    private static $instance;


    /**
     * コンストラクタ
     * IDとして生成日時のハッシュ値を作成
     */
    private function __construct()
    {
        $this->id = md5(date('r').mt_rand());
    }


    /**
     * 唯一のインスタンスを返すためのメソッド
     *
     * @return SingletonSampleインスタンス
     */
    public static function getInstance()
    {
        if (!isset(self::$instance)) {
            self::$instance = new SingletonSample();
            echo 'a SingletonSample instance was created!';
        }
        return self::$instance;
    }


    /**
     * IDを返す
     *
     * @return インスタンスのID
     */
    public function getID()
    {
        return $this->id;
    }


    /**
     * インスタンス複製を許可しない
     * @throws RuntimeException
     */
    final public function __clone()
    {
        throw new RuntimeException('Clone is not allowed against '.get_class($this));
    }
}
