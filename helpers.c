#include "helpers.h"
#include <math.h>
#include <string.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < round(width / 2); j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original[height][width];
    memcpy(&original, image, sizeof(RGBTRIPLE) * height * width);  //copy of original image

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int ofsetx[] = {-1, -1, -1, 0, 0, 0, 1, 1, 1}; //find it based on the 3x3 grid of pixels that surrounds that pixel
            int ofsety[] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
            float red = 0;
            float green = 0;
            float blue = 0;
            float counter = 0;

            for (int k = 0; k < 9; k++)
            {
                int nx = x + ofsetx[k];
                int ny = y + ofsety[k];

                if (nx >= 0 && nx < height && ny >= 0 && ny < width)
                {
                    counter++;
                    red += original[nx][ny].rgbtRed;
                    green += original[nx][ny].rgbtGreen;
                    blue += original[nx][ny].rgbtBlue;
                }
            }
            image[x][y].rgbtRed = round(red / counter);
            image[x][y].rgbtGreen = round(green / counter);
            image[x][y].rgbtBlue = round(blue / counter);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original[height][width];
    memcpy(&original, image, sizeof(RGBTRIPLE) * height * width);  //copy of original image

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int ofsetx[] = {-1, -1, -1, 0, 0, 0, 1, 1, 1}; //find it based on the 3x3 grid of pixels that surrounds that pixel
            int ofsety[] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
            int gx[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1}; //kernel
            int gy[] = {-1, -2, -1, 0, 0, 0, 1, 2, 1}; //kernel
            float red_gx = 0;
            float green_gx = 0;
            float blue_gx = 0;
            float red_gy = 0;
            float green_gy = 0;-
            float blue_gy = 0;

            for (int k = 0; k < 9; k++)
            {
                int nx = x + ofsetx[k];
                int ny = y + ofsety[k];

                if (nx >= 0 && nx < height && ny >= 0 && ny < width)
                {
                    red_gx += (original[nx][ny].rgbtRed * gx[k]);
                    green_gx += (original[nx][ny].rgbtGreen * gx[k]);
                    blue_gx += (original[nx][ny].rgbtBlue * gx[k]);
                    red_gy += (original[nx][ny].rgbtRed * gy[k]);
                    green_gy += (original[nx][ny].rgbtGreen * gy[k]);
                    blue_gy += (original[nx][ny].rgbtBlue * gy[k]);
                }
            }
            int red = round(sqrtf(pow(red_gx, 2) + pow(red_gy, 2)));
            int green = round(sqrtf(pow(green_gx, 2) + pow(green_gy, 2)));
            int blue = round(sqrtf(pow(blue_gx, 2) + pow(blue_gy, 2)));

            if (red > 255) //To make sure it's limited to 255
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }

            image[x][y].rgbtRed = red;
            image[x][y].rgbtGreen = green;
            image[x][y].rgbtBlue = blue;
        }
    }
    return;
}