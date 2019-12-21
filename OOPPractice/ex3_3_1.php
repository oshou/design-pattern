<?php

class Gear
{
    private $chainring;
    private $cog;

    function __construct($chainring, $cog)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
    }

    function chainring()
    {
        return $this->chainring;
    }

    function cog()
    {
        return $this->cog;
    }

    function gear_inches($diameter)
    {
        return $this->ratio() * $diameter;
    }

    function ratio()
    {
        return $this->chainring() / $this->cog();
    }
}

class Wheel
{
    private $rim;
    private $tire;
    private $gear;

    function __construct($rim, $tire, $chainring, $cog)
    {
        $this->rim = $rim;
        $this->tire = $tire;
        $this->gear = new Gear($chainring, $cog);
    }

    function rim()
    {
        return $this->rim;
    }

    function tire()
    {
        return $this->tire;
    }

    function gear()
    {
        return $this->gear;
    }

    function diameter()
    {
        return $this->rim() + ($this->tire() * 2);
    }

    function gear_inches()
    {
        $g = $this->gear();
        return $g->gear_inches($this->diameter());
    }
}

$w = new Wheel(26, 1.5, 52, 11);
echo $w->gear_inches() . "\n";
