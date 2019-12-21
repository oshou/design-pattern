<?php

class ObscuringReferences
{
    private $data;

    function __construct($data)
    {
        $this->data = $data;
    }

    function data()
    {
        return $this->data;
    }

    // this->dataの構造に依存したメソッド
    function diameters()
    {
        $data = [];
        foreach ($this->data() as $cell) {
            $data[] = $cell[0] + ($cell[1] * 2);
        }
        return $data;
    }
}

$data = [[622, 20], [622, 23], [559, 30], [559, 40]];
$or = new ObscuringReferences($data);
print_r($or->diameters());
