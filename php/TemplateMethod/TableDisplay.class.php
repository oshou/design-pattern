<?php

require_once('AbstractDisplay.class.php');

/**
 * Concreteクラス(具象クラス)
 */
class TableDisplay extends AbstractDisplay
{
    /**
     * ヘッダ表示用の具象メソッド
     */
    protected function displayHeader()
    {
        echo '<table border="1" cellpadding="2" cellspacing="2">';
    }


    /**
     * ボディ表示用の具象メソッド
     */
    protected function displayBody()
    {
        foreach ($this->getData() as $key => $value) {
            echo '<tr>';
            echo '<th>'.$key.'</th>';
            echo '<td>'.$value.'</td>';
            echo '</tr>';
        }
    }


    /**
     * フッタ表示用の具象メソッド
     */
    protected function displayFooter()
    {
        echo '</table>';
    }
}
