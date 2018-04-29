<?php

require_once 'AbstractDisplay.class.php';

/**
 * ConcreteClass
 */
class TableDisplay extends AbstractDisplay
{
    /**
     * ヘッダを表示する
     */
    protected function displayHeader()
    {
        echo '<table border="1" cellpadding="2" cellspacing="2">';
    }

    /**
     * ボディを表示する
     */
    protected function displayBody()
    {
        foreach ($this->getData() as $Key => $value){
            echo '<tr>';
            echo '<th>'.$key.'</th>';
            echo '<td>'.$value.'</td>';
            echo '</tr>';
        }
    }

    /**
     * フッタを表示する
     */
    protected function displayFooter()
    {
        echo '</table>';
    }
}
