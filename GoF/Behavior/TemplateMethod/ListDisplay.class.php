<?php

require_once('AbstractDisplay.class.php');

/**
 * Concreteクラス(具象クラス)
 */
class ListDisplay extends AbstractDisplay
{
    /**
     * ヘッダ表示用の具象メソッド
     */
    protected function displayHeader()
    {
        echo '<dl>';
    }


    /**
     * ボディ表示用の具象メソッド
     */
    protected function displayBody()
    {
        foreach ($this->getData() as $key => $value) {
            echo '<dt>Item '.$key.'</dt>';
            echo '<dd>'.$value.'</dd>';
        }
    }


    /**
     * フッタ表示表の具象メソッド
     */
    protected function displayFooter()
    {
        echo '</dl>';
    }
}
