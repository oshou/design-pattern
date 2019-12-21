<?php

class Gear
{
    private $chainring;
    private $cog;
    private $rim;
    private $tire;

    function __construct($chainring, $cog, $rim, $tire)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
        $this->rim = $rim;
        $this->tire = $tire;
    }

    // Readerメソッド
    function chainring()
    {
        return $this->chainring;
    }

    function cog()
    {
        return $this->cog;
    }

    function rim()
    {
        return $this->rim;
    }

    function tire()
    {
        return $this->tire;
    }

    function gear_inches()
    {
        $wheel = new Wheel($this->rim(), $this->tire());
        return $this->ratio() * $wheel->diameter();
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
}

$gear = new Gear(52, 11, 26, 1.5);
echo $gear->gear_inches() . "\n";
