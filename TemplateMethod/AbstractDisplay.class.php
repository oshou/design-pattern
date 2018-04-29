<?php
/**
 * AbstractClass
 */
abstract class AbstractDisplay
{
    /**
     * 表示するデータ
     */
    private $data;

    /**
     * constructor
     * @param mixed 表示するデータ
     */
    public function __construct($data)
    {
        if (!is_array($data)){
            $data = array($data);
        }
        $this->data = $data;
    }

    /**
     * TemplateMethod
     */
    public function display()
    {
        $this->displayHeader();
        $this->displayBody();
        $this->displayFooter();
    }

    /**
     * データを取得する
     */
    public function getData()
    {
        return $this->data;
    }

    /**
     * ヘッダを表示する
     */
    protected abstract function displayHeader();

    /**
     * ボディを表示する
     */
    protected abstract function displayBody();

    /**
     * フッタを表示する
     */
    protected abstract function displayFooter();
}
