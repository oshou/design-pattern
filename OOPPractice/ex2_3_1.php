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

    function ratio()
    {
        return $this->chainring / $this->cog;
    }
}
