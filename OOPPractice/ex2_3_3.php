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

    function diameters()
    {
        $data = [];
        foreach ($this->data() as $cell) {
            $data[] = $cell[0] + ($cell[1] * 2);
        }
        return $data;
    }
}

class RevealingReferences
{
    private $wheels;

    function __construct($data)
    {
        $this->wheels = $this->wheelify($data);
    }

    function wheels()
    {
        return $this->wheels();
    }

    function diameters()
    {
        $wheels = [];
        foreach ($this->wheels as $wheel) {
            $wheels[] = $wheel->rim + ($wheel->tire * 2);
        }
        return $wheels;
    }

    function wheelify($data)
    {
        $data = [];
        foreach ($this->data as $cell) {
            $data[] = new Wheel(cell[0],cell[1])
        }
        return $data;
    }
}

$data = [[622, 20], [622, 23], [559, 30], [559, 40]];
$or = new ObscuringReferences($data);
print_r($or->diameters());
