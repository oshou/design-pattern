<?php

class Gear
{
    private $chainring;
    private $cog;
    private $wheel;

    function __construct($chainring, $cog, $wheel = null)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
        $this->wheel = $wheel;
    }

    function chainring()
    {
        return $this->chainring;
    }

    function cog()
    {
        return $this->cog;
    }

    function wheel()
    {
        $result = $this->wheel;
        return $result;
    }

    function ratio()
    {
        return $this->chainring() / $this->cog();
    }

    function gear_inches()
    {
        return $this->ratio() * $this->wheel()->diameter();
    }
}

class Wheel
{
    function __construct($rim, $tire)
    {
        $this->rim = $rim;
        $this->tire = $tire;
    }

    function rim()
    {
        return $this->rim;
    }

    function tire()
    {
        return $this->tire;
    }

    function diameter()
    {
        return $this->rim() + ($this->tire() * 2);
    }

    function circumference()
    {
        return $this->diameter() * M_PI;
    }
}

$w1 = new Wheel(26, 1.5);
echo $w1->circumference() . PHP_EOL;

$g1 = new Gear(52, 11, $w1);
echo $g1->gear_inches() . PHP_EOL;

$g2 = new Gear(52, 11);
echo $g2->ratio() . PHP_EOL;
