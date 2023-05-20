using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class Gecis : MonoBehaviour
{
    
    public void CevapAnahtari(int c)
    {
        SceneManager.LoadScene(1);
    }

    public void Oyun(int o)
    {
        SceneManager.LoadScene(0);
    }
}
